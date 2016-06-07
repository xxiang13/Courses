var sections = document.getElementsByTagName('section');

for (var index = 0; index < sections.length; index++) {
    sections[index].onclick = handleClick; // asign function to each event for next use
}

function handleClick (event) {
    console.log('current element: ' + this.className + ' | target element: ' + event.target.className);

    if (this.className == 'regular') {
        event.stopPropagation();
        console.log('event propogation stopped');
    }
}