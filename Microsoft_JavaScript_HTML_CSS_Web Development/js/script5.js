
function handleClick(callback) {
    alert('This button has been clicked');
    if (callback) {
        callback();
    }
}

function doMore() {
    alert('I could process more logic here');
}

// Observe that all of the HTML content on the page is removed and replaced with the text "Test Message"
function doSomethingElse() {
    document.writeln('Test Message');
}