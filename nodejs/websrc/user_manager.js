// TODO remove this sample module later
function UserManager() {
    this.get_user = function(req, res) {
        user_data = [
            {name: '老王', age: 53},
            {name: '小明', age: 15}
        ];
        res.send(user_data);
    };
};

module.exports = UserManager;