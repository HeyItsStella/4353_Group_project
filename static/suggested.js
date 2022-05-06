function get_suggest()
{  
    //get data from front end using "ID" attribute
    var amount = document.getElementById("num-gallons").value;
    //var address2 = document.getElementById("inoutstate").innerHTML;
    var date=document.getElementById("date").value;
    var instate = document.getElementById("inoutstate").value;
    var reqb4 = document.getElementById("reqb4").value;
    var price = document.getElementById("price");
    var total =document.getElementById("total");

    
    finalNum =0;
    getsug =0;
    payme =0;
    var curDate = new Date(); //create current time object, this is in the form of date + time to milliseconds
    //var stDate = curDate.getFullYear()+'-'+(curDate.getMonth()+1)+'-'+curDate.getDate();  //convert date to xxxx-yy-zz formart
    var date2 = Date.parse(date);
    if(amount=='' || date=='' ){
        window.alert("Please enter valid amount and delivery date");
        return;
    }

    if(amount<=0){
        window.alert("Please enter valid amount");
        //window.alert(date.getTime());
        return;
    }

    
    if(date2 <= curDate){
        window.alert("Delivery date can not be in the past or today");
        return;

    }
      
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
       

        getsug1=1.5+finalNum;
        getsug2=getsug1.toFixed(2);

        payme=getsug2*amount;
        sum=payme.toFixed(2);//fix decimal to 2 places

        price.value=getsug2;
        total.value=sum;

/*
        var server_data =[
            {"amount":amount},
            {"date":date},
            {"instate":instate},
            {"reqb4":reqb4},
            {"price.value":price},
            {"total.value":total}
        ];
*/
        $.ajax({
            type: "POST",
            url: "/process_suggest", //maps to route decorator for a particualr function in python that processes the request
            //data: JSON.stringify(server_data), //convert JSON(javascript object notation) into srting format to transfer to the server
            contentType:"appplication/json",
            dataType: 'json',
        });
               
}