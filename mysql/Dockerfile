# MySQLの公式イメージを使用
FROM mysql:8.0

# 環境変数を設定
ENV MYSQL_DATABASE=test_db \
    MYSQL_USER=test \
    MYSQL_PASSWORD=test \
    MYSQL_ROOT_PASSWORD=root

# ポート3306を公開
EXPOSE 3306

# カスタム設定ファイルをイメージに追加（オプション）
# COPY custom.cnf /etc/mysql/conf.d/

# コンテナ起動時に実行するスクリプトを追加（オプション）
# COPY startup-script.sh /usr/local/bin/
# RUN chmod +x /usr/local/bin/startup-script.sh
# ENTRYPOINT ["startup-script.sh"]
# CMD ["mysqld"]

# デフォルトのエントリポイントとコマンドを使用
CMD ["mysqld"]
