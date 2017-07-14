const DSCClient = require("dscframework/clients/node");
const { Util } = require("dscframework");
const Cortex = require("./Cortex");

class CognitiveHub {

  constructor() {
    this.dsc = new DSCClient("ws://localhost:8080");
  }

  start() {
    this.dsc.start(()=>this.onStart());
    this.sentimentCortex = null;
  }

  onStart() {
    this.sentimentCortex = new Cortex("sentiment", this.dsc);
    this.running = true;
    this.dsc.register("message", {
      input: {},
      output: {}
    });
  }

  async getSentiment(text) {
    var data = {
      list: [text]
    };
    var raw = await this.sentimentCortex.run("message", data);
    var str = Util.uint8ToString(raw);
    return JSON.parse(str)[0][0];
  }

}

const hub = new CognitiveHub();
hub.start();
module.exports = hub;
