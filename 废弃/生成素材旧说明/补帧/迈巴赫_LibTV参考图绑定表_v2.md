# 迈巴赫TVC｜LibTV 参考图绑定表 v2

2026-10-11。逐节点回读「迈巴赫TVC｜驶出尼伯龙根｜导演工作版」后生成。叙事镜头 49 个；V31、V32、V38、V43 拆分后实际视频任务 53 个。

## 使用规则

- `Mixed 1` 为当前视频任务的首帧，`Mixed 2` 为尾帧；单图任务只有 `Mixed 1`。表中记录的是 LibTV 真实节点 ID 和已连线顺序。
- Hailuo 02 的首尾帧模式只允许两张图。身份母图、场景母图在本表中作为人工验收和后续支持多参考图模型的对照，不代表已连接到 Hailuo 02 视频节点。
- V31/V32/V38 各拆为两段，前段尾帧和后段首帧复用同一图片；V43 原已有 A/B 两段。不得把三张图同时塞给单个 Hailuo 02 任务。

| 任务 | 视频节点 | Mixed 1 节点 | Mixed 2 节点 | 身份母图 | 场景母图 |
|---|---|---|---|---|---|
| V01 | v-5o6H4YaCLj | i-geLxiK5GEa | i-4wu3DYmuLc | 迈巴赫62_三视图_v1 (i-1dp9wgPCQc) | S01_A城桥入口_场景母图_v1 (i-bRP6b9Yq0o) |
| V02 | v-PqmDDL3UiA | i-Q1Fu4945kL | — | 迈巴赫62_三视图_v1 (i-1dp9wgPCQc) | S01_A城桥入口_场景母图_v1 (i-bRP6b9Yq0o) |
| V03 | v-JPHwLELZet | i-KGlimmAhwJ | — | 迈巴赫62_三视图_v1 (i-1dp9wgPCQc) | S01_A城桥入口_场景母图_v1 (i-bRP6b9Yq0o) |
| V04 | v-FMeW1pOtxj | i-4QdjSGi3lQ | i-rX9kDg4bzh | 迈巴赫62_三视图_v1 (i-1dp9wgPCQc) | S02_暴雨钢架桥_场景母图_v1 (i-xilAzXTdXU) |
| V05 | v-X2VJCb2grc | i-Dy9sF4fqlg | i-QcuXPuWExj | 迈巴赫62_三视图_v1 (i-1dp9wgPCQc) | S02_暴雨钢架桥_场景母图_v1 (i-xilAzXTdXU) |
| V06 | v-AcCYA2Hm2w | i-b9kHvtYWA0 | i-m93iWFrYLJ | 楚子航_三视图_v3 (i-7xTmrNtLr6) | S05_副驾驶看驾驶位_母图_v1 (i-uTPtB5ErbK) |
| V07 | v-6fy0h5yw41 | i-TnLRLK2B1U | i-yadOyBq4el | 迈巴赫62_三视图_v1 (i-1dp9wgPCQc) | S11_桥梁高空俯拍_场景母图_v1 (i-UT2NExV3tz) |
| V08 | v-bd4dW9zJ12 | i-PvL6ZlpJ2e | i-50EnhJHg4R | 迈巴赫62_三视图_v1 (i-1dp9wgPCQc) | S02_暴雨钢架桥_场景母图_v1 (i-xilAzXTdXU) |
| V09 | v-ov8lSrnRx0 | i-7NMGb1OJl5 | — | 楚子航_三视图_v3 (i-7xTmrNtLr6) | S05_副驾驶看驾驶位_母图_v1 (i-uTPtB5ErbK) |
| V10 | v-uFM3SOYNZD | i-ZD5ninFtFc | i-OWaEDLuRNz | 奥丁_本体三视图_v3 (i-Z2jC9AFjlr)<br>八足马_黑色三视图_v5 (i-YuwogTXwZE)<br>奥丁长枪_全长与细节设定_v1 (i-zclCL8omvB) | S04_B城高塔_场景母图_v1 (i-51alDl5b64) |
| V11 | v-2lR6Kw9xNr | i-mMaPqt6WxF | i-dUN8BbTUz9 | 奥丁_本体三视图_v3 (i-Z2jC9AFjlr)<br>八足马_黑色三视图_v5 (i-YuwogTXwZE)<br>奥丁长枪_全长与细节设定_v1 (i-zclCL8omvB) | S04_B城高塔_场景母图_v1 (i-51alDl5b64) |
| V12 | v-dzH3hUmsqI | i-ib6yi9t2Wz | i-gpB0lyI6MH | 奥丁_本体三视图_v3 (i-Z2jC9AFjlr)<br>八足马_黑色三视图_v5 (i-YuwogTXwZE)<br>奥丁长枪_全长与细节设定_v1 (i-zclCL8omvB) | S04_B城高塔_场景母图_v1 (i-51alDl5b64) |
| V13 | v-ababYZgAaS | i-PrzFC5InN9 | i-AOy2ivDFrL | 奥丁_本体三视图_v3 (i-Z2jC9AFjlr)<br>八足马_黑色三视图_v5 (i-YuwogTXwZE)<br>奥丁长枪_全长与细节设定_v1 (i-zclCL8omvB) | S04_B城高塔_场景母图_v1 (i-51alDl5b64) |
| V14 | v-Zj3BA3LtEw | i-7WJ43pUnEv | i-sdveg0aFsl | 奥丁_本体三视图_v3 (i-Z2jC9AFjlr)<br>八足马_黑色三视图_v5 (i-YuwogTXwZE)<br>奥丁长枪_全长与细节设定_v1 (i-zclCL8omvB) | S04_B城高塔_场景母图_v1 (i-51alDl5b64) |
| V15 | v-5u5mVmZ6Ux | i-7xVX7Xveuo | i-bLozTVKg4L | 奥丁_本体三视图_v3 (i-Z2jC9AFjlr)<br>八足马_黑色三视图_v5 (i-YuwogTXwZE)<br>奥丁长枪_全长与细节设定_v1 (i-zclCL8omvB) | S04_B城高塔_场景母图_v1 (i-51alDl5b64) |
| V16 | v-uGVof99Lof | i-ARzldcR669 | i-09QqVRu9Xj | 奥丁_本体三视图_v3 (i-Z2jC9AFjlr)<br>八足马_黑色三视图_v5 (i-YuwogTXwZE)<br>奥丁长枪_全长与细节设定_v1 (i-zclCL8omvB) | S02_暴雨钢架桥_场景母图_v1 (i-xilAzXTdXU) |
| V17 | v-Y7t0cIQniV | i-NCPh7XG6wB | i-carEsnORgy | 奥丁_本体三视图_v3 (i-Z2jC9AFjlr)<br>八足马_黑色三视图_v5 (i-YuwogTXwZE)<br>奥丁长枪_全长与细节设定_v1 (i-zclCL8omvB) | S03_桥面侧向空间_场景母图_v1 (i-Cl8wCon9JM) |
| V18 | v-iV9K2FPgqC | i-GzELjK11yP | i-dO7VE9jXr8 | 奥丁_本体三视图_v3 (i-Z2jC9AFjlr)<br>八足马_黑色三视图_v5 (i-YuwogTXwZE)<br>奥丁长枪_全长与细节设定_v1 (i-zclCL8omvB) | S03_桥面侧向空间_场景母图_v1 (i-Cl8wCon9JM) |
| V19 | v-Wjwh3Iz2BF | i-raJks4kOmZ | — | 奥丁_本体三视图_v3 (i-Z2jC9AFjlr)<br>八足马_黑色三视图_v5 (i-YuwogTXwZE)<br>奥丁长枪_全长与细节设定_v1 (i-zclCL8omvB) | S03_桥面侧向空间_场景母图_v1 (i-Cl8wCon9JM) |
| V20 | v-kEXdpmwrF9 | i-5HcN5FVbHJ | i-iqZxZdgm5s | 楚子航_三视图_v3 (i-7xTmrNtLr6)<br>奥丁_本体三视图_v3 (i-Z2jC9AFjlr)<br>八足马_黑色三视图_v5 (i-YuwogTXwZE)<br>奥丁长枪_全长与细节设定_v1 (i-zclCL8omvB) | S06_驾驶员向前视角_母图_v1 (i-goOSR31r1k) |
| V21 | v-JdJ0RnIwwp | i-xA8Sh6aZoG | i-ryLAs2tr0x | 迈巴赫62_三视图_v1 (i-1dp9wgPCQc)<br>楚子航_三视图_v3 (i-7xTmrNtLr6) | S12_奥丁骑乘高度俯视_场景母图_v1 (i-Wqw5ZVHW0F) |
| V22 | v-S8JxJ1C61z | i-o8x1enmQOt | i-6s4531H79O | 楚子航_三视图_v3 (i-7xTmrNtLr6) | I02_油门与脚踏区_母图_v1 (i-9tfPa8dM43) |
| V23 | v-bkynsGA3LW | i-fyKc9xnsq6 | i-de1OqlP5Ui | 楚子航_三视图_v3 (i-7xTmrNtLr6) | I01_方向盘与仪表_母图_v1 (i-4OVA0Xjuny) |
| V24 | v-AKdLEO3FIW | i-wYSpq36MrX | i-eF00pxmPlI | 迈巴赫62_三视图_v1 (i-1dp9wgPCQc) | S02_暴雨钢架桥_场景母图_v1 (i-xilAzXTdXU) |
| V25 | v-3xVoTwAI0V | i-R5HmYQcyuO | i-ADFXXwYiJM | 迈巴赫62_三视图_v1 (i-1dp9wgPCQc)<br>奥丁_本体三视图_v3 (i-Z2jC9AFjlr)<br>八足马_黑色三视图_v5 (i-YuwogTXwZE)<br>奥丁长枪_全长与细节设定_v1 (i-zclCL8omvB) | S03_桥面侧向空间_场景母图_v1 (i-Cl8wCon9JM) |
| V26 | v-vLQZgVVMyr | i-DZ4HmPCMHo | — | 楚子航_三视图_v3 (i-7xTmrNtLr6) | S03_桥面侧向空间_场景母图_v1 (i-Cl8wCon9JM) |
| V27 | v-cB7UA95z1N | i-0v1xMpoNoV | — | 奥丁_本体三视图_v3 (i-Z2jC9AFjlr)<br>八足马_黑色三视图_v5 (i-YuwogTXwZE)<br>奥丁长枪_全长与细节设定_v1 (i-zclCL8omvB) | S03_桥面侧向空间_场景母图_v1 (i-Cl8wCon9JM) |
| V28 | v-EShNkhtIYy | i-Fa9zBuSjnh | i-hSQVa9NcKy | 迈巴赫62_三视图_v1 (i-1dp9wgPCQc)<br>奥丁_本体三视图_v3 (i-Z2jC9AFjlr)<br>八足马_黑色三视图_v5 (i-YuwogTXwZE)<br>奥丁长枪_全长与细节设定_v1 (i-zclCL8omvB) | S03_桥面侧向空间_场景母图_v1 (i-Cl8wCon9JM) |
| V29 | v-tV04EkHC8P | i-eNW9tkJ6L0 | — | 楚子航_三视图_v3 (i-7xTmrNtLr6) | S05_副驾驶看驾驶位_母图_v1 (i-uTPtB5ErbK) |
| V30 | v-Kov0vPoEON | i-LzTkHnws6m | i-l68LMBKKPB | 奥丁_本体三视图_v3 (i-Z2jC9AFjlr)<br>八足马_黑色三视图_v5 (i-YuwogTXwZE)<br>奥丁长枪_全长与细节设定_v1 (i-zclCL8omvB) | S03_桥面侧向空间_场景母图_v1 (i-Cl8wCon9JM) |
| V31 | v-TSUjchKe1j | i-DiUS3IY31v | i-uyPXMAuh42 | 奥丁_本体三视图_v3 (i-Z2jC9AFjlr)<br>八足马_黑色三视图_v5 (i-YuwogTXwZE)<br>奥丁长枪_全长与细节设定_v1 (i-zclCL8omvB) | S03_桥面侧向空间_场景母图_v1 (i-Cl8wCon9JM) |
| V31B | v-uPnp9SheV2 | i-uyPXMAuh42 | i-c0iCJaioi7 | 奥丁_本体三视图_v3 (i-Z2jC9AFjlr)<br>八足马_黑色三视图_v5 (i-YuwogTXwZE)<br>奥丁长枪_全长与细节设定_v1 (i-zclCL8omvB) | S03_桥面侧向空间_场景母图_v1 (i-Cl8wCon9JM) |
| V32 | v-amvAZT1skA | i-PiYn9cAxOa | i-dlfbgRLFdw | 迈巴赫62_三视图_v1 (i-1dp9wgPCQc)<br>奥丁_本体三视图_v3 (i-Z2jC9AFjlr)<br>八足马_黑色三视图_v5 (i-YuwogTXwZE)<br>奥丁长枪_全长与细节设定_v1 (i-zclCL8omvB) | S03_桥面侧向空间_场景母图_v1 (i-Cl8wCon9JM) |
| V32B | v-MXMEz4sjL7 | i-dlfbgRLFdw | i-p5Oj90n5gd | 迈巴赫62_三视图_v1 (i-1dp9wgPCQc)<br>奥丁_本体三视图_v3 (i-Z2jC9AFjlr)<br>八足马_黑色三视图_v5 (i-YuwogTXwZE)<br>奥丁长枪_全长与细节设定_v1 (i-zclCL8omvB) | S03_桥面侧向空间_场景母图_v1 (i-Cl8wCon9JM) |
| V33 | v-vjeCjzwKIg | i-wBC0r3DppX | i-FMNoBpUcM9 | 楚子航_三视图_v3 (i-7xTmrNtLr6)<br>奥丁_本体三视图_v3 (i-Z2jC9AFjlr)<br>八足马_黑色三视图_v5 (i-YuwogTXwZE)<br>奥丁长枪_全长与细节设定_v1 (i-zclCL8omvB) | I03_车内后视镜_母图_v1 (i-zwNA0Kns5Q) |
| V34 | v-0MHNYdbiHj | i-CRmZOUl90E | i-iKACJzqtVf | 楚子航_三视图_v3 (i-7xTmrNtLr6) | I02_油门与脚踏区_母图_v1 (i-9tfPa8dM43) |
| V35 | v-cbvWt2LrRV | i-ImhjbUht0a | i-p3QVkuZOEC | 迈巴赫62_三视图_v1 (i-1dp9wgPCQc)<br>奥丁_本体三视图_v3 (i-Z2jC9AFjlr)<br>八足马_黑色三视图_v5 (i-YuwogTXwZE)<br>奥丁长枪_全长与细节设定_v1 (i-zclCL8omvB) | S02_暴雨钢架桥_场景母图_v1 (i-xilAzXTdXU) |
| V36 | v-n90C4IW6XU | i-zIKnNpzaWY | i-QfOhJQUGd4 | 奥丁_本体三视图_v3 (i-Z2jC9AFjlr)<br>八足马_黑色三视图_v5 (i-YuwogTXwZE)<br>奥丁长枪_全长与细节设定_v1 (i-zclCL8omvB) | S02_暴雨钢架桥_场景母图_v1 (i-xilAzXTdXU) |
| V37 | v-CMbGUYSYd6 | i-Utu3JX5VoR | i-a8UevcOqK1 | 奥丁_本体三视图_v3 (i-Z2jC9AFjlr)<br>八足马_黑色三视图_v5 (i-YuwogTXwZE)<br>奥丁长枪_全长与细节设定_v1 (i-zclCL8omvB) | S02_暴雨钢架桥_场景母图_v1 (i-xilAzXTdXU) |
| V38 | v-CWmdGDsys4 | i-42ecabqd7N | i-3itVTIpfSH | 迈巴赫62_三视图_v1 (i-1dp9wgPCQc)<br>奥丁_本体三视图_v3 (i-Z2jC9AFjlr)<br>八足马_黑色三视图_v5 (i-YuwogTXwZE)<br>奥丁长枪_全长与细节设定_v1 (i-zclCL8omvB) | S02_暴雨钢架桥_场景母图_v1 (i-xilAzXTdXU) |
| V38B | v-PvhadrinaV | i-3itVTIpfSH | i-cCniyBHUOc | 迈巴赫62_三视图_v1 (i-1dp9wgPCQc)<br>奥丁_本体三视图_v3 (i-Z2jC9AFjlr)<br>八足马_黑色三视图_v5 (i-YuwogTXwZE)<br>奥丁长枪_全长与细节设定_v1 (i-zclCL8omvB) | S02_暴雨钢架桥_场景母图_v1 (i-xilAzXTdXU) |
| V39 | v-3A81cJTnbT | i-ek04mMT8Cv | i-DvUIe2HvH6 | 迈巴赫62_三视图_v1 (i-1dp9wgPCQc)<br>奥丁_本体三视图_v3 (i-Z2jC9AFjlr)<br>八足马_黑色三视图_v5 (i-YuwogTXwZE)<br>奥丁长枪_全长与细节设定_v1 (i-zclCL8omvB) | S02_暴雨钢架桥_场景母图_v1 (i-xilAzXTdXU) |
| V40 | v-JKP3FyxFuF | i-3Ra3J7dWFs | i-xeKkMgPR2a | 楚子航_三视图_v3 (i-7xTmrNtLr6) | I01_方向盘与仪表_母图_v1 (i-4OVA0Xjuny) |
| V41 | v-7ShJhsS7s1 | i-bNCuHb8GN2 | i-Q5AHE9j77b | 迈巴赫62_三视图_v1 (i-1dp9wgPCQc) | S02_暴雨钢架桥_场景母图_v1 (i-xilAzXTdXU) |
| V42 | v-sS9khjGXgO | i-eHAHjrjLWv | i-iRGGTnKSUv | 楚子航_三视图_v3 (i-7xTmrNtLr6) | S06_驾驶员向前视角_母图_v1 (i-goOSR31r1k) |
| V43A | v-7jzN3eikXx | i-9OVXNu1jhY | i-2JTWfuVQaN | 迈巴赫62_三视图_v1 (i-1dp9wgPCQc) | S07_水幕内侧_场景母图_v1 (i-8veyuJwmwl) |
| V43B | v-w27fsRGd66 | i-2JTWfuVQaN | i-RK2qTdI2lX | 迈巴赫62_三视图_v1 (i-1dp9wgPCQc) | S08_水幕外侧回望_场景母图_v1 (i-CfK8IRRN7I) |
| V44 | v-vMp4ZGJaWm | i-hbxGzzf9gj | i-22i4faPuxD | 奥丁_本体三视图_v3 (i-Z2jC9AFjlr)<br>八足马_黑色三视图_v5 (i-YuwogTXwZE)<br>奥丁长枪_全长与细节设定_v1 (i-zclCL8omvB) | S08_水幕外侧回望_场景母图_v1 (i-CfK8IRRN7I) |
| V45 | v-o4WHlzIFGX | i-zstVMMfFVx | i-P2k6K6UAyi | 楚子航_三视图_v3 (i-7xTmrNtLr6)<br>奥丁_本体三视图_v3 (i-Z2jC9AFjlr)<br>八足马_黑色三视图_v5 (i-YuwogTXwZE)<br>奥丁长枪_全长与细节设定_v1 (i-zclCL8omvB) | I03_车内后视镜_母图_v1 (i-zwNA0Kns5Q)<br>S08_水幕外侧回望_场景母图_v1 (i-CfK8IRRN7I) |
| V46 | v-rS02KsDYXw | i-eZ0rr0mlpP | — | 楚子航_三视图_v3 (i-7xTmrNtLr6) | S05_副驾驶看驾驶位_母图_v1 (i-uTPtB5ErbK) |
| V47 | v-t7qOkEfyjz | i-YeiCjE6Wt4 | i-LnMCVmFOZV | 迈巴赫62_三视图_v1 (i-1dp9wgPCQc) | S09_驶入B城雨后道路_场景母图_v1 (i-Di0NryZ0hv) |
| V48 | v-wsUpQ9vRrt | i-J9hW5XnZuA | — | 迈巴赫62_三视图_v1 (i-1dp9wgPCQc) | S10_东方晨光_场景母图_v1 (i-KEQwOxc05F) |
| V49 | v-EEO65RQDVO | i-f1mDTU3zZm | i-wwBG8MBCfK | 迈巴赫62_三视图_v1 (i-1dp9wgPCQc) | S10_东方晨光_场景母图_v1 (i-KEQwOxc05F) |
