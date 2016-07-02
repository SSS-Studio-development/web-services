
function get_phonetics(str){
  
  var xhr = new XMLHttpRequest();
  xhr.open("POST", "//localhost:5000/translate", true); // enter the actual URL for web-service here
  xhr.setRequestHeader("Access-Control-Allow-Origin", "*");
  xhr.setRequestHeader("Content-Type", "application/json; charset=UTF-8");
  xhr.send(JSON.stringify({"sentence":str}));


  xhr.onreadystatechange = processRequest;

  function processRequest(e)
  {
    if (xhr.readyState == 4)
    {
      console.log('pho trans set');
      phonetic_trans = xhr.responseText;
    }
  }

}

function anno_phonetic(xpath) {
    //if element is already translated
  if (anno_getElementByXpath(xpath).id != "phonetic" || !(anno_getElementByXpath(xpath).id)) {
    var text_to_translate = $j(anno_getElementByXpath(xpath)).html();
    get_phonetics(text_to_translate);
    var timer = window.setInterval
    (
      function ()
      {
        if(typeof phonetic_trans !== "default_value")
        {
          console.log("text changing");
          $j(anno_getElementByXpath(xpath)).text(phonetic_trans);
          phonetic_trans = "default_value";
          window.clearInterval(timer);
          $j(anno_getElementByXpath(xpath)).wrapInner("<span id='phonetic'></span>");
        }
        else
        {
          console.log("returned without change");
        }
      }
      ,1000
    );
  }
  else {
        console.log('already translated');
    }
}
