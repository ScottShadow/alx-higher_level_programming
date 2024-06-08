#!/usr/bin/node
$('DIV#red_header').click(function () {
    $('HEADER').addClass('red');
});
console.log($("HEADER").attr("class"));