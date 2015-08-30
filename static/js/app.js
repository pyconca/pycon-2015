$(function () {
    //mobile menu
    $("a[href=#menu]").click(function (e) {
        $(".menu").toggleClass("menu-open");
        e.preventDefault();
    });

    // messages
    $('.message .icon-cancel').click(function () {
        $(this).parent().slideUp(200);
    });
})
