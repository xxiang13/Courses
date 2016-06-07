var socket = new WebSocket('ws://echo.websocket.org');

// So the first thing we want to handle is the event ,when the socket opens.
// we're going to start a function, handle that event and we are basically going to show an alert
// or we can write in the "console.log( )".'Our socket has been opened'.
socket.onopen = function () {
    console.log('Our socket has been opened!');
}

// Next, we are going to add a another event handler and this is when we receive a message. 
// So we receive a message, we're going to get this event message from a socket essentially 
// we just want to call window.alert( ) and we're going to just 'event.data' . 
// So, just print out to the screen whatever message is sent. 
// This is the echo service, any messages we send to the socket just will be echo back to us.
socket.onmessage = function (event) {
    window.alert(event.data);
}

// So, in my JavaScript I'm going to create this function called "testMessage( )".
// And essentially this function is just kind a simply say, socket.send(" Hello World")
// Save. Now, we click this button, we're going to send this message via the websocket( ) ,
// we should expect that message to be echoed back.

// So, when we click the button it's going to now send "Hello World" message via the socket, we will continue and the own message
// event handler is fired because, the other side of websocket( ), responded immediately and received Hello World.
function testMessage () {
    socket.send("Hello World!");
}