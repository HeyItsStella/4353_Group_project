function get_suggest()
{  
    
     //get data from front end using "ID" attribute
    var amount = parseInt(document.getElementById("num-gallons").value);
    var instate = document.getElementById("inoutstate") ;
    var reqb4 = document.getElementById("reqb4") ;
    var price_back = document.getElementById("price");
    var total_back =document.getElementById("total");

/*

    if (amount>1000)
        GReqfactor =0.02;
    else
         GReqfactor=0.03;

    if (instate==True && reqb4 ==True)
        finalNum =(0.02-0.01+GReqfactor+0.1) * 1.5;
    else if (instate == False && reqb4 ==True)
        finalNum = (0.04-0.01+GReqfactor+0.1) * 1.5; 
    else if( instate ==True && reqb4==False)
        finalNum = (0.02+GReqfactor+0.1) * 1.5;
    else if (instate==False && reqb4 ==False)
        finalNum =(0.04+GReqfactor+0.1) * 1.5;
    
   // return finalNum;

   getsug=1.5+finalNum;
   payme=getsug*amount;
   payme.toFixed(2);//fix decimal

   price_back.innerHTML=getsug;
   total_back.innerHTML=payme;
*/
price_back.innerHTML=document.getElementById("num-gallons");
total_back.innerHTML=500;
   var server_data =[
       {"num-gallons":amount},
       {"inoutstate":instate},
       {"reqb4":reqb4},
       {"price":price_back},
       {"total":total_back}
   ];

   $.ajax({
       type: "POST",
       url: "/process_suggest", //maps to route decorator for a particualr function in python that processes the request
       data: JSON.stringify(server_data), //convert JSON(javascript object notation) into srting format to transfer to the server
       contentType:"appplication/json",
       dataType: 'json',
   });

}

/*
function get_suggest()
{
    var getsug=0;
    var price_back = document.getElementById("price");
    getsug=1.5+margin();

    price_back.innerHTML=getsug;
}

function get_total()
{
    var payme=0;
    var total_back =document.getElementById("total");
    payme=amount*get_suggest();
    payme.toFixed(2);

    total_back.innerHTML=payme;
}
*/