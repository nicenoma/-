# 随机密码生成器

这是一个简单而强大的随机密码生成器，可以生成包含大小写字母、数字和特殊符号的高强度密码。

## 功能特点

- 生成指定长度的随机密码（默认32位）
- 可自定义包含的字符类型（大写字母、小写字母、数字、特殊符号）
- 使用Python的`secrets`模块确保密码的随机性和安全性
- 简单易用的API，方便在其他项目中调用

## 运行环境

- Python 3.6+（推荐使用Python 3.8或更高版本）
- 无需安装额外的第三方库，仅使用Python标准库

## 使用方法

### 直接运行

```bash
# 直接运行脚本生成一个32位强密码
python passwd_generate.py
```

### 作为模块导入

```python
# 导入密码生成函数
from passwd_generate import generate_password, generate_strong_password

# 生成一个默认的32位强密码（包含所有字符类型）
password = generate_strong_password()
print(password)

# 生成一个自定义长度的密码
password = generate_strong_password(length=16)
print(password)

# 自定义字符类型
password = generate_password(
    length=20,
    include_uppercase=True,
    include_lowercase=True,
    include_digits=True,
    include_symbols=False  # 不包含特殊符号
)
print(password)
```

## 函数说明

### generate_password

```python
generate_password(length=32, include_uppercase=True, include_lowercase=True, include_digits=True, include_symbols=True)
```

**参数说明：**

- `length`：密码长度，默认为32位
- `include_uppercase`：是否包含大写字母，默认为True
- `include_lowercase`：是否包含小写字母，默认为True
- `include_digits`：是否包含数字，默认为True
- `include_symbols`：是否包含特殊符号，默认为True

**返回值：**

- 生成的随机密码字符串

### generate_strong_password

```python
generate_strong_password(length=32)
```

**参数说明：**

- `length`：密码长度，默认为32位

**返回值：**

- 生成的强密码字符串（包含所有字符类型）

## 安全提示

- 建议使用16位或更长的密码以提高安全性
- 对于重要账户，建议使用32位或更长的密码
- 不同账户应使用不同的密码
- 建议使用密码管理器安全存储生成的密码
- 定期更换重要账户的密码