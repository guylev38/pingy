/*
Remove the annyoing import error.

Author: guylev38
Date: 24/09/2025
*/

declare module "*.vue" {
  import { DefineComponent } from "vue";
  const component: DefineComponent<{}, {}, any>;
  export default component;
}
