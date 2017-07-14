const { Command } = require("discord.js-commando");
const CognitiveHub = require("../../cognitive/CognitiveHub");

module.exports = class SentimentCommand extends Command {

  constructor(client) {
    super(client, {
      name: "sentiment",
      group: "test",
      memberName: "sentiment",
      description: "Parses sentiment",
      examples: ["sentiment"],
      args: [
        {
          key: "text",
          prompt: "Sentence to extract sentiment from",
          type: "string"
        }
      ]
    });
  }

  async run(msg, args) {
    const { text } = args;
    var sentiment = await CognitiveHub.getSentiment(text);


    console.log("got sentiment", sentiment);
    return msg.say("sentiment: " + sentiment);
  }

};
