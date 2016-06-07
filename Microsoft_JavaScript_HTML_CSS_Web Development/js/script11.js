var slideInterval = 3500;

//retrieve all of the figure elements within the section element using the id of carousel. 
//Return the resulting array as the result of this function.
function getFigures() {
    return document.getElementById('carousel').getElementsByTagName('figure');
}


//This function iterates over the figure elements in the section element. 
//It removes the visible class from the current figure element, then adds 
//the class to the next figure element. Once complete, it uses the setTimeout 
//function to invoke itself again after a specified amount of time (3500 milliseconds = 3.5 seconds).
function moveForward() {
    var pointer;
    var figures = getFigures();
    for (var i = 0; i < figures.length; i++) {
        if (figures[i].className == 'visible') {
            figures[i].className = '';
            pointer = i;
        }
    }
    if (++pointer == figures.length) {
        pointer = 0;
    }
    figures[pointer].className = 'visible';
    setTimeout(moveForward, slideInterval);
}

//use the setTimeout function in JavaScript to 
//invoke the moveForward method after a specified amount of time. 
//Use the slideInterval variable for the time interval.
function startPlayback() {    
    setTimeout(moveForward, slideInterval);
}

// The JavaScript logic simply adds the visible CSS class to the next image in the rotation approximately every 3.5 seconds.
startPlayback();