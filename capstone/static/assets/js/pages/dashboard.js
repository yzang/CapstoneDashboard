/**
 * Created by Yiming on 3/27/2016.
 */
$(function () {
    //initialize the map size
    var mapHeight = $('#mapPanel').css('height')
    $('#map').css('height', mapHeight)

    var customNouiToolTipYear = $.Link({
        target: '-tooltip-<div class="noui-tooltip"></div>',
        method: function (value) {
            $(this).html('<span class="text-semibold">' + value + '</span>');
        }
    });
    $(".noui-slider-year").noUiSlider({
        start: [2014, 2016],
        connect: true,
        range: {
            'min': 2011,
            'max': 2016
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

    $(".noui-slider-day").noUiSlider({
        start: [1, 7],
        connect: true,
        range: {
            min: 1,
            max: 7
        },
        step: 1,
        serialization: {
            lower: [customNouiToolTipMonth, $.Link({
                target: $("#noui-tooltip-day1"),
            })],
            upper: [customNouiToolTipMonth, $.Link({target: $("#noui-tooltip-day2")})],
            format: {
                decimals: 0,
            }
        }
    })

    $(".noui-slider-hour").noUiSlider({
        start: [1, 24],
        connect: true,
        range: {
            min: 1,
            max: 24
        },
        step: 1,
        serialization: {
            lower: [customNouiToolTipMonth, $.Link({
                target: $("#noui-tooltip-hour1"),
            })],
            upper: [customNouiToolTipMonth, $.Link({target: $("#noui-tooltip-hour2")})],
            format: {
                decimals: 0,
            }
        }
    })

    // Basic initialization
    $('.multiselect').multiselect({});

})


function getFilters() {
    var params = {}
    params['year_from'] = parseInt($("#noui-tooltip-year1").html())
    params['year_to'] = parseInt($("#noui-tooltip-year2").html())
    params['month_from'] = parseInt($("#noui-tooltip-month1").html())
    params['month_to'] = parseInt($("#noui-tooltip-month2").html())
    params['day_from'] = parseInt($("#noui-tooltip-day1").html())
    params['day_to'] = parseInt($("#noui-tooltip-day2").html())
    params['hour_from'] = parseInt($("#noui-tooltip-hour1").html())
    params['hour_to'] = parseInt($("#noui-tooltip-hour2").html())
    params['injury_options']=$('#injury-select').val()
    params['collision_options']=$('#collision-select').val()
    return params
}

function renderMap(params) {
    // render the map
    $('#map').block({
        message: '<i class="icon-spinner9 spinner"></i>',
        overlayCSS: {
            backgroundColor: '#1B2024',
            opacity: 0.35,
            cursor: 'wait'
        },
        css: {
            border: 0,
            padding: 0,
            backgroundColor: 'none',
            color: '#fff'
        }
    });
    setTimeout(function () {
        $.ajax({
            url: '/capstone/api/getMajorOrFatal',
            method: 'post',
            dataType: 'json',
            data: params,
            success: function (data) {
                offersMapInit("map", data)
                $('#map').unblock();
            }
        })
    }, 3000)
}