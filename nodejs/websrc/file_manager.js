var fs = require('fs');
var multer = require('multer');
var path = require('path');

// TODO move into config file
var uploadDir = './public/upload/'; // 设置文件上传路径
var maxSize = 1024*1024*5; // 设置文件大小限制
var upload = multer({
    dest:uploadDir,
    limits: {
	    //fileSize: maxSize, // 限制文件大小 (这里不要限制，而是在后面的代码中手动控制)
		files: 1, // 限制上传数量
	}}).single('file');

function FileManager () {
    // 文件上传
    this.upload = function (req, res) {        
        upload(req, res, function (err) {
            if(err) {
                console.error(err.message);
            } else {
                var file_path = req.file.path; // 临时文件路径
                var file_type = req.file.mimeType; // 文件类型
                var file_originalname = req.file.originalname //文件原始名
                var des_file = uploadDir + file_originalname; // 拼接成存储在服务器的文件路径
                var file_extname = path.extname(file_originalname);
                
                // 控制台打印文件信息
                console.log('临时文件路径：%s', file_path);                 
                console.log('文件类型：%s', file_type); 
                console.log('原始文件名：%s', file_originalname); 
                console.log('文件后缀名：%s',file_extname);
                
                fs.readFile(file_path, function(err, data) { // 读取临时文件
                    if (file_extname != '.xlsx' && file_extname != '.xls') {
                        var response = {
                            code: -1, 
                            message: '请上传 Excel 文档 (后缀为 xlsx 或 xls)'
                        };                            
                        fs.unlink(req.file.path,function(err) { //删除临时文件
                            if(err){
                                console.error(err.message);
                            } else {
                                console.log('成功删除非 Excel 文件');
                            }
                        });
                        res.end(JSON.stringify(response));
                        return;                            
                    } else {
                        var file_size = req.file.size; // 文件大小
                        console.log('文件大小：%s', file_size/1024,'kb');
                        if (file_size > maxSize){ // 检查大小
                            var response = {
                                code: -2, 
                                message: '请勿上传超过指定大小的文件'
                            };
                            fs.unlink(req.file.path,function(err) { // 删除临时文件
                                if(err){
                                    console.error(err.message);
                                } else {
                                    console.log('成功删除超大文件');
                                }
                            });
                            res.end(JSON.stringify(response));
                            return;
                        }else {
                            // 上传的文件通过格式检查，将 data 保存到（服务器上）一个新的文件中
                            fs.writeFile(des_file, data, function(err) {
                                if(err) {
                                    console.error(err.message);
                                } else {
                                    var response = {
                                        code: 0, 
                                        message: '文件上传成功',
                                        filename: file_originalname
                                    };
                                    console.log('文件上传成功');
                                    // 删除临时文件
                                    fs.unlink(req.file.path,function(err) {
                                        if(err){
                                            console.error(err.message);
                                        }else{
                                            console.log('成功删除临时文件');
                                        }
                                    });
                                }
                                res.end(JSON.stringify(response));
                            });
                        }
                    }
                });
            }        
        });
    };
};

module.exports = FileManager;
