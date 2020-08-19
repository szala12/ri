var botui = new BotUI('my-bot');
// var server_url = " {% bot_data.get('SERVER_URL') %}"
console.log(server_url);
botui.message.add({
    content: 'AAAAAAAAAAAAAAAAAAAAA!'
}).then(function () { // wait till previous message has been shown.

    botui.message.add({
        delay: 1000,
        human: true,
        content: 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA!'
    });
});