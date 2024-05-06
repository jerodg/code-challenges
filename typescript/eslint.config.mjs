import js from "@eslint/js";
import styleGuide from "eslint-config-google";

export default [
    js.configs.recommended,
    ...[].concat(styleGuide)
];
