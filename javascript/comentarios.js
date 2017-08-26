window.fbAsyncInit = function() {
  FB.init({
    appId            : '1856889521294651',
    autoLogAppEvents : true,
    xfbml            : true,
    version          : 'v2.10'
  });
  FB.AppEvents.logPageView();
};
(function(d, s, id){
   var js, fjs = d.getElementsByTagName(s)[0];
   if (d.getElementById(id)) {return;}
   js = d.createElement(s); js.id = id;
   js.src = "//connect.facebook.net/pt_BR/sdk.js";
   fjs.parentNode.insertBefore(js, fjs);
 }(document, 'script', 'facebook-jssdk'));
