# Operation APIs for SIL's audio‐visual device

## 概要

SILの視聴覚機器をHTTP経由で操作するためのAPIです。

TODO: もっとちゃんと書く

## 使い方

```bash
$ curl http://{api-endpoint-url}/hogehoge
```

## API定義

- `/hdmi_msw/version`: HDMIマトリクススイッチャーのファームウェアバージョンをチェックする（デバッグ用）
- `/hdmi_msw/in/{input_port}/out/{output_port}`: HDMIマトリクススイッチャーのインプットとアウトプットを変更する
- `/pj/{logical_projector_name}/power/status`: プロジェクターの電源の状態を確認する
- `/pj/{logical_projector_name}/power/on`: プロジェクターの電源を入れる
- `/pj/{logical_projector_name}/power/off`: プロジェクターの電源を切る
 