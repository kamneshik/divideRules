import base64
import json


def get_user_id_from_jwt_token(jwt_token: str) -> str:
    token_parts = jwt_token.split('.')
    payload_bytes = base64.urlsafe_b64decode(token_parts[1] + "==")
    payload = payload_bytes.decode('utf-8')

    payload_dict = json.loads(payload)
    user_id = payload_dict.get("sub")

    return user_id


if __name__ == "__main__":
    uid = get_user_id_from_jwt_token(
        "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9."
        "eyJzdWIiOiI0NTYxMjM3OSIsIm5hbWUiOiJNYWtzaW0gS29yb2xldiIsImlhdCI6MTUxNjIzOTAyMn0."
        "WertK-kpnBXhJ1oiAy9O-NSmgvmwpFlOSP8kTpC-SR4")
