function correctMethodName() {  
    return "Output Message";
}

//var result = correctMethodName(3);

try {
    var result = wrongMethodName(3);
    document.writeln(result);
}
catch (error) {
    document.writeln('<h3>Error:&nbsp;</h3><p>' + error + "</p>");    

}


