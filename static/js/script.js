function switchRightWhite() {
    fetch("/switch_right_central")
}
function switchLeftWhite() {
    fetch("/switch_left_central")
}

function allWhite() {
    fetch("/switch_all_central")
}

function switchBarColor() {
    fetch("/switch_bar_color")
}

function allLight() {
    fetch("/all_light")
}

function switchRightColor() {
    fetch("/switch_right_central")
}

function switchLeftColor() {
    fetch("/switch_left_central")
}

function switchAllColor() {
    fetch("/switch_all_color")
}
$(function() {
    let hoverColor = "#ffb1aa"
    let active = "#00FF00";
    let passive = "#b9b9b9"
    let mapPinClass = {}
    function setStatusAll() {

    }

    function flash(elm) {
        $(elm).stop()
            .animate({'stroke-dashoffset': 0}, 500)
            .css({'fill': 'white', 'transition': 'fill 1s'});
        setTimeout((elm) => {
            $(elm).stop()
                .animate({'stroke-dashoffset': 0}, 500)
                .css({'fill': 'transparent', 'transition': 'fill 1s'});
        })
    }
    $('rect.clickable, path.clickable, image.clickable').hover(function() {
        $(this).stop()
            .animate({'stroke-dashoffset': 0}, 1000)
            .css({'fill': hoverColor, 'transition': 'fill 1s'});
        console.log('on');
    }, function() {
        $(this).stop()
            .animate({'stroke-dashoffset': 900}, 1000)
            .css({'fill': passive, 'transition': 'fill 1s'});
    });

    $("[fill]").attr('fill', passive);
    $(".color_bar").click(function () {
        fetch("/switch_bar_color");
        flash(this)
    });

    $(".white_left").click(function () {
        fetch("/switch_left_central")
    });

    $(".white_right").click(function () {

        fetch("/switch_right_central")
    });

    $(".color_left").click(function () {
        fetch("/switch_left_color")
    });

    $(".color_right").click(function () {
        fetch("/switch_right_color")
    });

    $(".rad1").click(function () {
        fetch("/switch_rad1")
    });

    $(".rad2").click(function () {
        fetch("/switch_rad2")
    });

    $(".volet_down").click(function () {
        fetch("/voletdown")
    });

    $(".volet_stop").click(function () {
        fetch("/voletstop")
    });

    $(".volet_up").click(function () {
        fetch("/voletup")
    });

    $(".alllight").click(function () {
        fetch("/switch_all_light")
    });
});