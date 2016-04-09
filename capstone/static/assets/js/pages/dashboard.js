/**
 * Created by Yiming on 3/27/2016.
 */
$(function () {
    google.maps.event.addDomListener(window, 'load', init);
    function init() {
        $.getJSON('/static/assets/demo_data/data.json').done(function (json) {
            offersMapInit("map", json);
        })
    }

    //initialize the map size
    var mapHeight=$('#mapPanel').css('height')
    console.log(mapHeight)
    $('#map').css('height',mapHeight)

    var customNouiToolTipYear = $.Link({
        target: '-tooltip-<div class="noui-tooltip"></div>',
        method: function (value) {
            $(this).html('<span class="text-semibold">' + value + '</span>');
        }
    });
    $(".noui-slider-year").noUiSlider({
        start: [2014, 2015],
        connect: true,
        range: {
            'min': 2010,
            'max': 2020
        },
        serialization: {
            lower: [customNouiToolTipYear, $.Link({target: $("#noui-tooltip-year1")})],
            upper: [customNouiToolTipYear, $.Link({target: $("#noui-tooltip-year2")})],
            format: {decimals: 0}
        }
    });

    var months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
    var customNouiToolTipMonth = $.Link({
        target: '-tooltip-<div class="noui-tooltip"></div>',
        method: function (value) {
            $(this).html('<span class="text-semibold">' + months[value - 1] + '</span>');
        }
    });

    $(".noui-slider-month").noUiSlider({
        start: [1, 12],
        connect: true,
        range: {
            min: 1,
            max: 12
        },
        step: 1,
        serialization: {
            lower: [customNouiToolTipMonth, $.Link({
                target: $("#noui-tooltip-month1"),
            })],
            upper: [customNouiToolTipMonth, $.Link({target: $("#noui-tooltip-month2")})],
            format: {
                decimals: 0,
            }
        }

    })


})
