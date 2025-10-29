// 主JavaScript文件
// 基础功能和通用交互逻辑

// 等待DOM加载完成
document.addEventListener('DOMContentLoaded', function() {
    // 这里可以添加通用的交互逻辑
    console.log('商品展示网站已加载');
    
    // 搜索框功能
    const searchForm = document.querySelector('.search-box');
    if (searchForm) {
        searchForm.querySelector('button').addEventListener('click', function() {
            const searchQuery = searchForm.querySelector('input').value.trim();
            if (searchQuery) {
                console.log('搜索:', searchQuery);
                // 实际项目中可以跳转到搜索结果页面
            }
        });
        
        // 按下回车搜索
        searchForm.querySelector('input').addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                const searchQuery = this.value.trim();
                if (searchQuery) {
                    console.log('搜索:', searchQuery);
                    // 实际项目中可以跳转到搜索结果页面
                }
            }
        });
    }
});