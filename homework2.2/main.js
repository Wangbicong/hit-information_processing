/**
 * Created by wangbicong on 2017/5/12.
 */

classA = [19, 18, 18, 15, 18, 11, 16, 19, 17, 17, 20, 17, 19, 20, 20, 15, 15, 16]
classB = [19, 15, 20, 20, 17, 18, 18, 15, 16, 18, 15, 19, 20, 19, 19, 16, 17, 13, 15]

var myChart = echarts.init(document.getElementById('main'));

// 指定图表的配置项和数据
var option = {
    title: {
        text: '直方图'
    },
    tooltip: {},
    legend: {
        data:['人数']
    },
    xAxis: {
        data: classA
    },
    yAxis: {},
    series: [{
        name: '人数',
        type: 'bar'
    }]
};

// 使用刚指定的配置项和数据显示图表。
myChart.setOption(option);