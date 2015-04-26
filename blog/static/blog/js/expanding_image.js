var hiddenHeight = 100;
var prepareSpeed = 1500;
var showHideSpeed = 400;

$(document).ready(function() {
    prepareImages();

    $(".expanding-image-wrapper").ready(function() {
        prepareImages();
    });

    $(".expanding-image-wrapper").click(function() {
        if ($(this).hasClass("hiding"))
            showImage($(this));
        else
            hideImage($(this));
    });
});

function prepareImages() {
    $(".expanding-image-wrapper").each(function(index) {
        $(this).find("img").load(function() {
            var imgHeight = $(this).height();
            $(this).parent().css("height", hiddenHeight + "px");
            $(this).animate({ top: -imgHeight/2 }, prepareSpeed);
        });
    });
}

function stopAnimation(obj) {
    $(obj).stop();
    $(obj).find("img").stop();
}

function showImage(obj) {
    stopAnimation($(obj));

    $(document).find(".expanding-image-wrapper").each(function() {
        if ($(this) != $(obj) && !$(this).hasClass("hiding")) {
            var imgHeight = $(this).find("img").height();
            $(this).find("img").animate({ top: -imgHeight/2 }, showHideSpeed);
            $(this).animate({ height: hiddenHeight }, showHideSpeed);
            $(this).addClass("hiding");
        }
    });

    var imgHeight = $(obj).find("img").height();
    $(obj).find("img").animate({ top: 0 }, showHideSpeed);
    $(obj).animate({ height: imgHeight }, showHideSpeed);
    $(obj).removeClass("hiding");
}

function hideImage(obj) {
    stopAnimation($(obj));
    var imgHeight = $(obj).find("img").height();
    $(obj).find("img").animate({ top: -imgHeight/2 }, showHideSpeed);
    $(obj).animate({ height: hiddenHeight }, showHideSpeed);
    $(obj).addClass("hiding");
}
