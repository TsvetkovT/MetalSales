/**
 * Created by TT on 9.12.17 г..
 */


function reSize() {
    var n = $("body").width() / 15;
	$("h1").css('fontSize', n + "pt");
	$("h3").css('fontSize', (n/20) * 4.2 + "pt");
	}
$(window).on("resize", reSize);
$(document).ready(reSize);

(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o), m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');  ga('create', 'UA-70761127-6', 'auto');  ga('send', 'pageview');