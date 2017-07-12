const Commando = require("discord.js-commando");
const path = require("path");
const sqlite = require("sqlite");

const { OWNER, PREFIX, TOKEN } = process.env;

const client = new Commando.Client({
  owner: OWNER
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
