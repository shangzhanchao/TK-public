import { defineComponent } from 'vue';

export default defineComponent({
  name: 'FooterSection',
  template: `
    <footer class="bg-gray-800 text-gray-200 py-8 px-4 text-sm">
      <div class="max-w-5xl mx-auto grid grid-cols-1 md:grid-cols-3 gap-4">
        <div>
          <h3 class="font-semibold mb-2">公司信息</h3>
          <p>营业执照链接</p>
          <p>ICP备案号</p>
        </div>
        <div>
          <h3 class="font-semibold mb-2">快速导航</h3>
          <ul>
            <li><a href="#" class="hover:underline">机器人本体</a></li>
            <li><a href="#" class="hover:underline">核心零部件</a></li>
            <li><a href="#" class="hover:underline">租赁服务</a></li>
          </ul>
        </div>
        <div>
          <h3 class="font-semibold mb-2">联系方式</h3>
          <p>邮箱: contact@example.com</p>
          <p>微博 | 微信公众号 | B站</p>
        </div>
      </div>
    </footer>
  `
});
