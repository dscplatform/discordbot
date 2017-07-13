const Commando = require("discord.js-commando");
const path = require("path");
const sqlite = require("sqlite");

const { OWNERS, PREFIX, TOKEN } = process.env;

const client = new Commando.Client({
  owner: OWNERS.split(","),
  commandPrefix: PREFIX,
  unknownCommandResponse: false,
  disableEveryone: true
});

client.registry
.registerGroups([
  ["test", "test commands"]
])
.registerDefaults()
.registerCommandsIn(path.join(__dirname, "commands"));

client.setProvider(
  sqlite.open(path.join(__dirname, "settings.sqlite3")).then((db) => new Commando.SQLiteProvider(db))
).catch(console.error);

client.login(TOKEN);
