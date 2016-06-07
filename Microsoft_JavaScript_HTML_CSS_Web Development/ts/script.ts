class Alert {

	//public method named showDialog with no return value
    public showDialog() {
        var message: string;
        message = this.getMessage();
        alert(message);
    }
    //private method named getMessage that returns a string
    private getMessage(): string {
        return 'Hello World';
    }
}

function showAlert() {
    var alertManager = new Alert(); //create a new instance of the Alert class and store it in a variable named alertManager
    alertManager.showDialog(); // invoke the showDialog method of your alertManager variable.
}