for(let i = 1; i <= 100; i++){

    let msg = "";

    if(i % 3 == 0)
        msg = "Fizz";

    if(i % 5 == 0)
        msg += "Buzz";

    if(msg == "")
        msg = i.toString();
    
    console.log(msg);
}