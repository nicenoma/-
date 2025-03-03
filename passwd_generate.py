import secrets
import string

def generate_password(length=32, include_uppercase=True, include_lowercase=True, 
                     include_digits=True, include_symbols=True):
    """
    生成一个随机密码
    
    参数:
        length (int): 密码长度，默认为32位
        include_uppercase (bool): 是否包含大写字母，默认为True
        include_lowercase (bool): 是否包含小写字母，默认为True
        include_digits (bool): 是否包含数字，默认为True
        include_symbols (bool): 是否包含特殊符号，默认为True
        
    返回:
        str: 生成的随机密码
    """
    # 定义字符集
    chars = ""
    if include_uppercase:
        chars += string.ascii_uppercase
    if include_lowercase:
        chars += string.ascii_lowercase
    if include_digits:
        chars += string.digits
    if include_symbols:
        chars += "!@#$%^&*()_+-=[]{}|;:,.<>?/~"
    
    # 确保至少选择了一种字符类型
    if not chars:
        raise ValueError("至少需要选择一种字符类型（大写字母、小写字母、数字或特殊符号）")
    
    # 生成密码
    password = ''.join(secrets.choice(chars) for _ in range(length))
    
    return password


def generate_strong_password(length=32):
    """
    生成一个强密码，包含大小写字母、数字和特殊符号
    
    参数:
        length (int): 密码长度，默认为32位
        
    返回:
        str: 生成的强密码
    """
    return generate_password(length=length)


if __name__ == "__main__":
    # 生成一个32位的强密码并打印
    password = generate_strong_password()
    print("生成的32位强密码:")
    print(password)