var worker; //define a worker variable

function startWorker() {  //function to start a worker
    worker = new Worker("js/mod4_worker.js");
    worker.onmessage = function(event) {
        document.getElementById("output").innerHTML += '<li>' + event.data + '</li>';
    };
}

function stopWorker() { //function to stop a worker
    worker.terminate();
}
