import java.io.IOException;
import org.apache.hadoop.hbase.conf;

public class Hbase{
    static Configuration conf = null;
    static {
        conf = HBaseConfiguration.create();
        conf.set("hbase.zookeeper.quorum","localhost");
    }


}
