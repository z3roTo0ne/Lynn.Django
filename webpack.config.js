var webpack = require('webpack');
var commonsPlugin = new webpack.optimize.CommonsChunkPlugin('common.js');
new webpack.DefinePlugin({
  "process.env": {
     NODE_ENV: JSON.stringify("development")
   }
});


module.exports = {
    entry: {
        hello: './static/jsx_src/hello.jsx',
        test: './static/jsx_src/test.jsx',
        duty: './static/jsx_src/duty.jsx',
        grid: './static/jsx_src/grid.jsx',
        study: './static/jsx_src/study.jsx',
        es6: './static/jsx_src/es6.jsx'
    },
    output: {
        path: './static/dist',
        //publicPath: '/var/www'   //网站运行时的路径
        //filename: '[name].bundle.js' // 如果这样写，name的值是entry的key，这里也就是hello，最终hello.bundle.js
        filename: '[name].bundle.js'
    },
    resolve: {
        //查找module的话从这里开始查找
        //root: '/home/develop/code/projectconfig/static/',

        //自动扩展文件后缀名，意味着我们require模块可以省略不写后缀名
        extensions: ['', '.js', '.jsx'],

        //模块别名定义，方便后续直接引用别名，无须多写长长的地址
        //alias: {
        //    AppStore : 'js/stores/AppStores.js',//后续直接 require('AppStore') 即可
        //    ActionType : 'js/actions/ActionType.js',
        //    AppAction : 'js/actions/AppAction.js'
        //}

        modulesDirectories: ['node_modules']
    },
    module: {
        //多个loader之间用“!”连接起来
        loaders: [
            {
                test: /\.js$/,
                loader: 'babel-loader',
                exclude: '/node_modules/',
                query: {
                    compact: false
                }
            },
            {
                test: /\.jsx$/,
                //loader: 'babel-loader!jsx-loader?harmony',
                loader: 'babel-loader',
                exclude: '/node_modules/',
                query: {
                    presets: ['es2015', 'react'], //使用babel-loader的时候要配置这个玩意, es2015=ES6
                    compact: true
                }
            }
        ]
    },
    plugins: [commonsPlugin],
    externals: {
        "jquery": "jQuery",
        // //don't bundle the 'react' npm package with our bundle.js
        // //but get it from a global 'React' variable
        'react': 'React',
        'react-dom': 'ReactDOM'
    },
    watch: true //开启watch模式
};

//webpack 最基本的启动webpack命令
//webpack -w 提供watch方法，实时进行打包更新
//webpack -p 对打包后的文件进行压缩
//webpack -d 提供SourceMaps，方便调试
//webpack --colors 输出结果带彩色，比如：会用红色显示耗时较长的步骤
//webpack --profile 输出性能数据，可以看到每一步的耗时
//webpack --display-modules 默认情况下 node_modules 下的模块会被隐藏，加上这个参数可以显示这些被隐藏的模块