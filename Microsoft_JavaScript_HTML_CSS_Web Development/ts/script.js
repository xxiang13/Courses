var Alert = (function () {
    function Alert() {
    }
    Alert.prototype.showDialog = function () {
        var message;
        message = this.getMessage();
        alert(message);
    };
    Alert.prototype.getMessage = function () {
        return 'Hello World';
    };
    return Alert;
}());
function showAlert() {
    var alertManager = new Alert();
    alertManager.showDialog();
}