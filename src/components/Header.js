import { defineComponent, ref } from 'vue';

export default defineComponent({
  name: 'HeaderSection',
  setup() {
    const keywords = ref('');
    const suggestions = ref([]);
    function search() {
      console.log('Searching:', keywords.value);
      // TODO: connect to backend search API
    }
    return { keywords, suggestions, search };
  },
  template: `
    <header class="bg-white shadow p-4 flex items-center justify-between">
      <div class="text-xl font-bold">机器人企业</div>
      <nav class="space-x-4 hidden md:block">
        <a href="#" class="hover:text-blue-600">首页</a>
        <a href="#" class="hover:text-blue-600">机器人本体</a>
        <a href="#" class="hover:text-blue-600">核心零部件</a>
        <a href="#" class="hover:text-blue-600">租赁服务</a>
        <a href="#" class="hover:text-blue-600">解决方案</a>
        <a href="#" class="hover:text-blue-600">关于我们</a>
      </nav>
      <div class="flex items-center space-x-2">
        <input v-model="keywords" @keyup.enter="search" placeholder="搜索" class="border rounded px-2 py-1" />
        <button @click="search" class="bg-blue-600 text-white px-3 py-1 rounded">搜索</button>
      </div>
    </header>
  `
});
