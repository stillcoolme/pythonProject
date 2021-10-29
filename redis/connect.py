from rediscluster import RedisCluster


class RedisClusterClient():

    def __init__(self):
        self.startup_nodes = []
        self.client = None

    def get_redis_client(self, nodes):
        """
        Returns a RedisCluster connection.
        """
        if not self.client:
            redis_cluster_list = nodes.split(',')
            for redis_node in redis_cluster_list:
                redis_node_list = redis_node.split(':')
                self.startup_nodes.append({
                    "host": redis_node_list[0],
                    "port": int(redis_node_list[1])
                })
            try:
                self.client = RedisCluster(
                    startup_nodes=self.startup_nodes,
                    skip_full_coverage_check=False
                )
            except Exception as general_error:
                raise Exception(
                    'Failed to create RedisCluster client, error: {error}'.format(
                        error=str(general_error)
                    )
                )
        return self.client