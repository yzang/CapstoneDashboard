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
            x:70,
            x2:80,
            y:80,
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
            x:70,
            x2:80,
            y:80,
            y2: 100,// y2可以控制 X轴跟Zoom控件之间的间隔，避免以为倾斜后造成 label重叠到zoom上
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
            x:80,
            x2:80,
            y:80,
            y2: 60,// y2可以控制 X轴跟Zoom控件之间的间隔，避免以为倾斜后造成 label重叠到zoom上
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
            x:80,
            x2:80,
            y:80,
            y2: 60,// y2可以控制 X轴跟Zoom控件之间的间隔，避免以为倾斜后造成 label重叠到zoom上
        },

    })
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
            max: Math.round(series[0].max * 1.1),
            axisLabel: {
                formatter: '{value}'
            },
            splitLine: {show: false},
        },
            {
                type: 'value',
                name: series[1].legend,
                min: 0,
                max: Math.round(series[1].max * 1.1),
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
                max: Math.round(series[i].max * 1.1),
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
                max: Math.round(series[i].max * 1.1),
                splitLine: {show: false},
                splitArea: {show: false},
                scale: true
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
            start: 20,
            end: 80
        }]
    })
}

$(function(){
    var collision_type_chart = init_collision_type_chart();
    collision_type_chart.showLoading();
    $.ajax({
        url: "/capstone/api/getCrashByCollisionType",
        method: "get",
        dataType: "json",
        success: function (data) {
            collision_type_chart.hideLoading();
            build_collision_type_chart(collision_type_chart, data)
        }
    });


    //set up intersection chart
    var intersection_chart = init_intersection_type_chart();
    intersection_chart.showLoading();
    $.ajax({
        url: "/capstone/api/getCrashByIntersectionType",
        method: "get",
        dataType: "json",
        success: function (data) {
            intersection_chart.hideLoading();
            build_intersection_type_chart(intersection_chart, data)
        }
    });

    //set up monthly crash chart
    var monthly_crash_chart = init_monthly_crash_chart();
    monthly_crash_chart.showLoading();
    $.ajax({
        url: "/capstone/api/getCrashByMonth",
        method: "get",
        dataType: "json",
        success: function (data) {
            monthly_crash_chart.hideLoading();
            build_monthly_crash_chart(monthly_crash_chart, data)
        }
    });


    //resize
    // Resize charts
    // ------------------------------
    window.onresize = function () {
        setTimeout(function () {
            collision_type_chart.resize();
            intersection_chart.resize();
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
        hidden = !hidden
    })
})