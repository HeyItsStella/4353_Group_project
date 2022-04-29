function get_suggest()
{  
    
    //get data from front end using "ID" attribute
    var amount = document.getElementById("num-gallons").value;
    //var address2 = document.getElementById("inoutstate").innerHTML;
    var date2=document.getElementById("date").value;
    var instate = document.getElementById("inoutstate").value;
    var reqb4 = document.getElementById("reqb4").value;
    var price_back = document.getElementById("price");
    var total_back =document.getElementById("total");

    
    finalNum =0;
    getsug =0;
    payme =0;

    if(amount=='' || date2=='' ){
        window.alert("Please enter amount and delivery date");
        return;
    }

    else {
        
        if (amount>1000)
            {GReqfactor =0.02;}
        else
            {GReqfactor=0.03;}

        if (instate== "True" && reqb4 =="True"){
            finalNum =(0.02-0.01+GReqfactor+0.1) * 1.5;}
        else if (instate === "False" && reqb4 === "True"){
            finalNum = (0.04-0.01+GReqfactor+0.1) * 1.5;}
        else if( instate === "True" && reqb4=== "False"){
            finalNum = (0.02+GReqfactor+0.1) * 1.5;}
        else if (instate==="False" && reqb4 ==="False"){
            finalNum =(0.04+GReqfactor+0.1) * 1.5;}
        //else
        //  finalNum = 100000;
        
        // return finalNum;

        getsug=1.5+finalNum;
        payme=getsug*amount;
        sum=parseFloat(payme).toFixed(2);//fix decimal to 2 places

        //instate+="love";
        //address2+="hate";
        price_back.value=getsug;
        total_back.value=sum;


        var server_data =[
            {"amount":amount},
            {"date":date},
            {"instate":instate},
            {"reqb4":reqb4},
            {"price_back.value":price_back},
            {"total_back.value":total_back}
        ];

        $.ajax({
            type: "POST",
            url: "/process_suggest", //maps to route decorator for a particualr function in python that processes the request
            data: JSON.stringify(server_data), //convert JSON(javascript object notation) into srting format to transfer to the server
            contentType:"appplication/json",
            dataType: 'json',
        });
        }       
}