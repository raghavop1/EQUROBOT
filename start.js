
const TelegramBot = require('node-telegram-bot-api');

// Replace 'YOUR_TELEGRAM_BOT_TOKEN' with your actual bot token obtained from the BotFather
const token = config.BOT_TOKEN

// Create a bot that uses 'polling' to fetch new updates
const bot = new TelegramBot(token, { polling: true });

// Listen for the /start command
bot.onText(/\/start/, (msg) => {
  const chatId = msg.chat.id;

  // Send a welcome message to the chat
  bot.sendMessage(chatId, 'Welcome to the bot! Type /help for a list of available commands.');
});

// Listen for any other kind of message
bot.on('message', (msg) => {
  const chatId = msg.chat.id;

  // Send a message to the chat acknowledging receipt of their message
  bot.sendMessage(chatId, 'Received your message!');
});
