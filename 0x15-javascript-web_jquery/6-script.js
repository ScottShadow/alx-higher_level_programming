#!/usr/bin/node
$('DIV#update_header').click(function () {
    $('HEADER').text('New Header!!!');
    console.log($("HEADER").text());
});