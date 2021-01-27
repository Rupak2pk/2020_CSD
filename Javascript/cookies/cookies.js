<!DOCTYPE html>
<html>
<head>
<script>
var myCookies={};

function saveCookies() {

myCookies["_user"] = document.getElementById("user").value;
myCookies["_age"] = document.getElementById("uage").value;

//Reusable Code

document.cookie = "";
var expiresDate = new Date(Date.now() +60*10000).toString();

//String
var cookieString = "";

for(var key in myCookies) {
cookieString = key + "=" + myCookies[key] + ";" + expiresDate + ";";
document.cookie = cookieString;
}

//End Reusable

document.getElementById("out").innerHTML = document.cookie;
}

//Loading Cookies

function loadCookies()

//Reusable Code

myCookies = {};
var kv = document.cookie.split(";");

for(var id in kv) {
var cookie = kv[id].split("=");
myCookies[cookie[0].trim()] = cookie[1];
}

//End Reusable

document.getElementById("user").value = myCookies["_user"];
document.getElementById("age").value = myCookies["_uage"];




</script>
</head>

<input type="text" id="user">
<input type="text" id="age">

<button onClick="saveCookies()">Save</button>

<button onClick="loadCookies()">Pull</button>

<p id="out"></p>




</html>
