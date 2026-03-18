# Upload Examples

## Minimal

```python
receipt = client.upload_document("sample.pdf")
print(receipt.document_id)
```

## Advanced

```python
receipt = client.upload_document("sample.pdf")
print("queued:", receipt.status)
```
