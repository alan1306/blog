var a;
var b;
function captchaValidation(){
    inputValue=parseInt(document.getElementById("captchainput").value)
    console.log(inputValue,a,b);
    if(inputValue==a+b){
        document.getElementById("submitButton").disabled=false;
        return true
    }
    else{
        document.getElementById("submitButton").disabled=true;
        alert("Enter a valid captcha");
        return false;
    }
}
function captcha(){
    a=Math.floor(Math.random()*10);
    b=Math.floor(Math.random()*10);

    document.getElementById("captcha").value=a.toString()+'+'+b.toString()+'= ?';

}
