
function get_suggest()
{  
    
     //get data from front end using "ID" attribute
    var amount = parseInt(document.getElementById("num-gallons").value);
    var instate = document.getElementById("inoutstate").innerHTML;
    var reqb4 = parseInt(document.getElementById("reqb4").innerHTML);
    var price_back = document.getElementById("price");
    var total_back =document.getElementById("total");

    finalNum =0;
    getsug =0;
    payme =0;

    if (amount>1000)
        {GReqfactor =0.02;}
    else
        {GReqfactor=0.03;}


    if (instate==1 && reqb4 ==1){
        finalNum =(0.02-0.01+GReqfactor+0.1) * 1.5;}
    else if (instate == 0 && reqb4 ==1){
        finalNum = (0.04-0.01+GReqfactor+0.1) * 1.5;}
    else if( instate ==1 && reqb4==0){
        finalNum = (0.02+GReqfactor+0.1) * 1.5;}
    else if (instate==0 && reqb4 ==0){
        finalNum =(0.04+GReqfactor+0.1) * 1.5;}
    //else
      //  finalNum = 100000;
    
   // return finalNum;

   getsug=1.5+finalNum;
   payme=getsug*amount;
   payme.toFixed(2);//fix decimal

   instate+="love";
   price_back.innerHTML=instate;
   total_back.innerHTML=payme;

/*
if(instate==0 && reqb4==0)
    finalNum=200;

else
    finalNum= 1000;


price_back.innerHTML=finalNum;
total_back.innerHTML=500;
*/
    

   var server_data =[
       {"amount":amount},
       {"instate":instate},
       {"reqb4":reqb4},
       {"price_back.innerHTML":price_back},
       {"total_back.innerHTML":total_back}
   ];

   $.ajax({
       type: "POST",
       url: "/process_suggest", //maps to route decorator for a particualr function in python that processes the request
       data: JSON.stringify(server_data), //convert JSON(javascript object notation) into srting format to transfer to the server
       contentType:"appplication/json",
       dataType: 'json',
   });

}

