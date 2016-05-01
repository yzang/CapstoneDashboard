/**
 * Created by Yiming on 4/23/2016.
 */

function init_collision_type_chart() {
    var chart = echarts.init(document.getElementById('collision_type_chart'), 'roma');
    chart.setOption({
        title: {
            text: 'Collision Type Analysis',
            x: 'left',
            textStyle: {
                color: '#000'
            }
        },
        tooltip: {
            trigger: 'axis',
            axisPointer: {            // 坐标轴指示器，坐标轴触发有效
                type: 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
            }
        }, grid: { // 控制图的大小，调整下面这些值就可以，
            x: 70,
            x2: 80,
            y: 80,
            y2: 100,// y2可以控制 X轴跟Zoom控件之间的间隔，避免以为倾斜后造成 label重叠到zoom上
        },
    })
    return chart
}

function init_intersection_type_chart() {
    var chart = echarts.init(document.getElementById('intersection_type_chart'), 'macarons');
    chart.setOption({
        title: {
            text: 'Intersection Type Analysis',
            x: 'left',
            textStyle: {
                color: '#000',
                fontWeight: 'bold'
            },
        },
        tooltip: {
            trigger: 'axis',
            axisPointer: {            // 坐标轴指示器，坐标轴触发有效
                type: 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
            }
        },
        grid: { // 控制图的大小，调整下面这些值就可以，
            x: 70,
            x2: 100,
            y: 70,
            y2: 150,// y2可以控制 X轴跟Zoom控件之间的间隔，避免以为倾斜后造成 label重叠到zoom上
        },
    })
    return chart
}

function init_monthly_crash_chart() {
    var chart = echarts.init(document.getElementById('crash_chart'), 'shine');
    chart.setOption({
        title: {
            text: 'Crash Severity Analysis',
            x: 'left',
            textStyle: {
                color: '#000',
                fontWeight: 'bold'
            },
        },
        tooltip: {
            trigger: 'axis',
            axisPointer: {            // 坐标轴指示器，坐标轴触发有效
                type: 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
            }
        },
        grid: { // 控制图的大小，调整下面这些值就可以，
            x: 80,
            x2: 80,
            y: 80,
            y2: 80,// y2可以控制 X轴跟Zoom控件之间的间隔，避免以为倾斜后造成 label重叠到zoom上
        },

    })
    return chart
}

function init_pie_bar_chart() {
    var chart = echarts.init(document.getElementById('pie_bar_chart'), 'macarons');
    return chart
}

function build_collision_type_chart(chart, data) {
    var series = data.series;
    var labels = data.labels;
    if (series.length <= 1) return
    chart.setOption({
        legend: {
            x: 'right',
            data: [series[0].legend, series[1].legend]
        },
        xAxis: {
            data: labels,
            type: 'category',
            axisLabel: {
                interval: 0,
                rotate: 45,
                margin: 2,
                textStyle: {
                    color: "#222"
                }
            }, splitLine: {show: false},
        },
        yAxis: [{
            type: 'value',
            name: series[0].legend,
            min: series[0].min,
            max: Math.ceil((series[0].max * 1.1) / 100.0) * 100,
            axisLabel: {
                formatter: '{value}'
            },
            splitLine: {show: false},
        },
            {
                type: 'value',
                name: series[1].legend,
                min: 0,
                max: Math.ceil((series[1].max * 1.1) / 100.0) * 100,
                axisLabel: {
                    formatter: '{value}'
                },
                splitLine: {
                    show: false,
                },
            }],
        series: [{
            name: series[0].legend,
            type: 'bar',
            data: series[0].data,

        }, {
            name: series[1].legend,
            type: 'line',
            yAxisIndex: 1,
            data: series[1].data,
            smooth: true,
            lineStyle: {
                normal: {
                    width: 3,
                    shadowColor: 'rgba(0,0,0,0.4)',
                    shadowBlur: 10,
                    shadowOffsetY: 10
                }
            },
        }]
    })
}

function build_intersection_type_chart(chart, data) {
    var series = data.series;
    var labels = data.labels;
    if (series.length <= 1) return
    var legend_data = {
        x: 'right',
        bottom:10,
        itemGaph:5,
        data: []}
    var yAxis_data = []
    var series_data = []
    for (var i = 0; i < series.length; i++) {
        legend_data.data.push(series[i].legend);
        if (i <= 1) {
            yAxis_data.push({
                type: 'value',
                name: series[i].legend,
                min: 0,
                max: Math.ceil((series[i].max * 1.1) / 10.0) * 10,
                splitLine: {show: false},
                splitArea: {show: false}

            })
        }
        series_data.push({
            name: series[i].legend,
            type: i == 0 ? 'bar' : 'line',
            data: series[i].data,
            yAxisIndex: i == 0 ? 0 : 1,
            smooth: true,
            lineStyle: {
                normal: {
                    width: 4,
                    shadowColor: 'rgba(0,0,0,0.4)',
                    shadowBlur: 10,
                    shadowOffsetY: 10
                }
            },

        })
    }
    chart.setOption({
        legend: legend_data,
        xAxis: {
            data: labels,
            type: 'category',
            axisLabel: {
                interval: 0,
                rotate: 45,
                margin: 2,
                textStyle: {
                    color: "#222"
                }
            },
            splitLine: {show: false},
        },
        yAxis: yAxis_data,
        series: series_data
    })
}

function build_monthly_crash_chart(chart, data) {
    var series = data.series;
    var labels = data.labels;
    if (series.length <= 1) return
    var legend_data = {x: 'right', data: []}
    var yAxis_data = []
    var series_data = []
    for (var i = 0; i < series.length; i++) {
        legend_data.data.push(series[i].legend);
        if (i <= 1) {
            yAxis_data.push({
                type: 'value',
                name: series[i].legend,
                min: 0,
                max: Math.ceil((series[i].max * 1.1) / 10.0) * 10,
                splitLine: {show: false},
                splitArea: {show: false},
            })
        }
        series_data.push({
            name: series[i].legend,
            type: i == 0 ? 'bar' : 'line',
            data: series[i].data,
            yAxisIndex: i == 0 ? 0 : 1,
            smooth: true,

            lineStyle: {
                normal: {
                    width: 3,
                    shadowColor: 'rgba(0,0,0,0.4)',
                    shadowBlur: 10,
                    shadowOffsetY: 10
                }
            },

        })
    }
    chart.setOption({
        legend: legend_data,
        xAxis: {
            data: labels,
            type: 'category',
            splitLine: {show: false},
        },
        yAxis: yAxis_data,
        series: series_data,
        dataZoom: [{
            show: true,
            realtime: true,
            start: 0,
            end: 100
        }]
    })
}

function build_pie_bar_chart(chart, data) {
    var years = data.years
    years.push("total")
    var person_types = data.person_types
    var age_ranges = data.age_ranges
    var max_2 = data.max[1]
    var series_config = []
    for (var i = 0; i < person_types.length; i++) {
        series_config.push({
            name: person_types[i],
            type: 'bar'
        })
    }
    series_config.push({
        name: 'Vehicle Type',
        type: 'pie',
        center: ['82%', '32%'],
        radius: '40%',
        tooltip: {
            formatter: "{a} <br/>{b}: {c} ({d}%)"
        },
        itemStyle: {
            normal: {
                shadowColor: 'rgba(0, 0, 0, 0.5)',
                shadowBlur: 7,
                shadowOffsetX: 2,
                shadowOffsetY: 2,
            }
        }
    })
    var baseOption = {
        tooltip: {},
        legend: {
            x: 'right',
            data: person_types
        },
        calculable: true,
        grid: {
            top: 90,
            bottom: 80,
            x: 150,
            x2: 250,
        },
        xAxis: [{
            'type': 'category',
            'axisLabel': {'interval': 0},
            'data': age_ranges,
            splitLine: {show: false}
        }],
        yAxis: [
            {
                type: 'value',
                name: 'Crash Count',
                max: Math.ceil((max_2 * 1.1) / 100.0) * 100,
                splitLine: {show: false},
                splitArea: {show: false},
            }
        ],
        timeline: {
            axisType: 'category',
            autoPlay: true,
            playInterval: 2500,
            symbolSize: 14,
            data: years
        },
        series: series_config
    }
    var options = []
    for (var i = 0; i < years.length - 1; i++) {
        var series_data = data[years[i]]
        options.push({
            title: {
                text: "Year " + years[i] + " Analysis by Age & Vehicle",
                textStyle: {
                    color: '#000',
                    fontWeight: 'bold'
                }
            },
            series: series_data,
            stack: "persons"
        })
    }
    options.push({
        title: {
            text: "All Years Data",
            textStyle: {
                color: '#000',
                fontWeight: 'bold'
            }
        },
        series: data.total,
        stack: ""
    })
    chart.setOption({
        baseOption: baseOption,
        options: options
    })
}
var collision_type_chart = init_collision_type_chart();
var intersection_chart = init_intersection_type_chart();
var monthly_crash_chart = init_monthly_crash_chart();
var pie_bar_chart = init_pie_bar_chart();
$(function () {
    var params = {}
    params['year_from'] = parseInt($("#noui-tooltip-year1").html())
    params['year_to'] = parseInt($("#noui-tooltip-year2").html())
    params['month_from'] = parseInt($("#noui-tooltip-month1").html())
    params['month_to'] = parseInt($("#noui-tooltip-month2").html())
    params['day_from'] = parseInt($("#noui-tooltip-day1").html())
    params['day_to'] = parseInt($("#noui-tooltip-day2").html())
    params['hour_from'] = parseInt($("#noui-tooltip-hour1").html())
    params['hour_to'] = parseInt($("#noui-tooltip-hour2").html())
    params['injury_options'] = $('#injury-select').val()
    params['collision_options'] = $('#collision-select').val()
    buildAllCharts(params)
    // Resize charts
    // ------------------------------
    window.onresize = function () {
        setTimeout(function () {
            collision_type_chart.resize();
            intersection_chart.resize();
            monthly_crash_chart.resize();
            pie_bar_chart.resize();
        }, 200);
    }

    var hidden = false
    $('#btn-collapse-sidebar').click(function () {
        if (!hidden) {
            $('#div-sidebar').hide()
        } else {
            $('#div-sidebar').show()
        }
        collision_type_chart.resize();
        intersection_chart.resize();
        monthly_crash_chart.resize();
        pie_bar_chart.resize();
        hidden = !hidden
    })
})

function buildAllCharts(params) {
    collision_type_chart.showLoading();
    $.ajax({
        url: "/capstone/api/getCrashByCollisionType",
        method: "post",
        dataType: "json",
        data: params,
        success: function (data) {
            collision_type_chart.hideLoading();
            build_collision_type_chart(collision_type_chart, data)
        }
    });
    intersection_chart.showLoading();
    $.ajax({
        url: "/capstone/api/getCrashByIntersectionType",
        method: "post",
        dataType: "json",
        data: params,
        success: function (data) {
            intersection_chart.hideLoading();
            build_intersection_type_chart(intersection_chart, data)
        }
    });
    monthly_crash_chart.showLoading();
    $.ajax({
        url: "/capstone/api/getCrashByMonth",
        method: "post",
        dataType: "json",
        data: params,
        success: function (data) {
            monthly_crash_chart.hideLoading();
            build_monthly_crash_chart(monthly_crash_chart, data)
        }
    });
    pie_bar_chart.showLoading();
    $.ajax({
        url: "/capstone/api/getCrashByVehicleAndAge",
        method: "get",
        dataType: "json",
        success: function (data) {
            pie_bar_chart.hideLoading()
            build_pie_bar_chart(pie_bar_chart, data)
        }
    })
}