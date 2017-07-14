
class Cortex {

  constructor(name, client) {
    this.name = name;
    this.client = client;
    this.buffer = new Map();
    this.init();
  }

  init() {
    this.client.subscribe(this.name, (head, data) => this.onMessage(head, data));
  }

  onMessage(head, data) {
    var chain = head.ch, len = head.ch.length, i = 0;
    var guid = null;
    for(; i < len; i++) {
      guid = chain[i];
      if (this.buffer.has(guid)) {
        this.buffer.get(guid)(data);
        this.buffer.delete(guid);
      }
    }
  }

  async run(output, data) {
    return new Promise((resolve, reject) => this.buffer.set(this.client.broadcast(output, null, data), resolve));
  }

}

module.exports = Cortex;
