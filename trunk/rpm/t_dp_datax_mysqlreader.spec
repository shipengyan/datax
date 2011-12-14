summary:t_dp_datax_mysqlreader
Name:t_dp_datax_mysqlreader
Version: 1.0.0
Release: 1
Group: :t_dp
License: Commercial

BuildArchitectures: noarch
Requires: t_dp_datax_engine

%description
datax
%{_svn_path}
%{_svn_revision}

%prep
cd ${OLDPWD}/../
export LANG=zh_CN.UTF-8
/home/ads/tools/apache-ant-1.7.1/bin/ant dist
%build

%install
mkdir -p .%{_prefix}/datax/plugins/reader/mysqlreader

cp ${OLDPWD}/../src/com/taobao/datax/plugins/reader/mysqlreader/ParamKey.java .%{_prefix}/datax/plugins/reader/mysqlreader
cp ${OLDPWD}/../build/plugins/mysqlreader-1.0.0.jar .%{_prefix}/datax/plugins/reader/mysqlreader
cp ${OLDPWD}/../build/plugins/plugins-common-1.0.0.jar .%{_prefix}/datax/plugins/reader/mysqlreader
cp -r ${OLDPWD}/../libs/mysql-connector-java-5.1.18-bin.jar .%{_prefix}/datax/plugins/reader/mysqlreader
cp -r ${OLDPWD}/../libs/commons-dbcp-1.4.jar .%{_prefix}/datax/plugins/reader/mysqlreader
cp -r ${OLDPWD}/../libs/commons-pool-1.5.4.jar .%{_prefix}/datax/plugins/reader/mysqlreader
cp -r ${OLDPWD}/../libs/commons-logging-1.1.1.jar .%{_prefix}/datax/plugins/reader/mysqlreader

%files
%defattr(0755,taobao,cug-tbdp)
%{_prefix}

%changelog
* Fri Aug 20 2010 meining 
- Version 1.0.0
- svn tag address
- http://svn.simba.taobao.com/svn/DW/arch/trunk/cheetah/services/datax/tools/dataexchange
