// file.cpp

#include <cerrno>
#include <sys/ioctl.h>

#include "file.h"


File& File::operator=( const File& rhs )
{
    if ( &rhs != this )
    {
        if ( m_nDescriptor == -1 )
	        m_nDescriptor = dup( rhs.m_nDescriptor );
        else
	        m_nDescriptor = dup2( rhs.m_nDescriptor, m_nDescriptor );
    }
    return *this;
}


int File::Open( const char *pName, int flags )
{
  if ( m_nDescriptor != -1 )
    return -1;

  if ( flags & O_CREAT )
    return EINVAL;

  if ( (m_nDescriptor = open( pName, flags )) == -1 )
    return errno;

  return 0;
}


int File::Create( const char *pName, int flags, mode_t mode )
{
  if ( m_nDescriptor != -1 )
    return -1;

  if ( (m_nDescriptor = open( pName, flags | O_CREAT, mode )) == -1 )
    return errno;

  return 0;
}


int File::Close()
{
    if ( m_nDescriptor != -1 )
    {
        if ( close( m_nDescriptor ) != 0 )
	        return errno;
        else
	        m_nDescriptor = -1;
    }

  return 0;
}


int File::Seek( off_t Offset, int iWhence, off_t& Result ) const
{
  off_t SeekResult = Seek( Offset, iWhence );

  if ( SeekResult == -1 )
    return errno;

  Result = SeekResult;
  return 0;
}


int File::Read( void *pv, size_t BytesToRead, size_t& BytesRead ) const
{
  ssize_t Result = Read( pv, BytesToRead );
  if ( Result == -1 )
    return errno;

  BytesRead = Result;
  return 0;
}


int File::Write( const void *pv, size_t BytesToWrite, size_t& BytesWritten ) const
{
  ssize_t Result = Write( pv, BytesToWrite );
  if ( Result == -1 )
    return errno;

  BytesWritten = Result;
  return 0;
}


bool File::CloseOnExec() const
{
  int iRetVal;

  if ( (iRetVal = fcntl( m_nDescriptor, F_GETFD )) == -1 )
    return false;

  return iRetVal & FD_CLOEXEC;
}


int File::GetFlags( int& flags ) const
{
  int iRetVal;

  if ( (iRetVal = fcntl( m_nDescriptor, F_GETFL )) == -1 )
    {
      flags = 0;
      return errno;
    }

  flags = iRetVal;
  return 0;
}


int File::SetFlags( int flags ) const
{
  if ( fcntl( m_nDescriptor, F_SETFL, long(flags) ) != 0 )
    return errno;

  return 0;
}


bool File::IsReadable() const
{
  int flags;

  if ( GetFlags( flags ) != 0 )
    return false;

  flags &= O_ACCMODE;
  return flags == O_RDONLY || flags == O_RDWR;
}


bool File::IsWritable() const
{
  int flags;

  if ( GetFlags( flags ) != 0 )
    return false;

  flags &= O_ACCMODE;
  return flags == O_WRONLY || flags == O_RDWR;
}


bool File::IsReadWritable() const
{
  int flags;

  if ( GetFlags( flags ) != 0 )
    return false;

  return (flags & O_ACCMODE) == O_RDWR;
}


bool File::Append() const
{
  int flags;

  if ( GetFlags( flags ) != 0 )
    return false;

  return flags & O_APPEND;
}


void File::Append( bool fAppend ) const
{
  int flags;

  if ( GetFlags( flags ) != 0 )
    return;

  if ( fAppend )
    flags |= O_APPEND;
  else
    flags &= ~O_APPEND;

  SetFlags( flags );
}


bool File::NonBlocking() const
{
  int flags;

  if ( GetFlags( flags ) != 0 )
    return false;

  return flags & O_NONBLOCK;
}


void File::NonBlocking( bool fNonBlock ) const
{
  int flags;

  if ( GetFlags( flags ) != 0 )
    return;

  if ( fNonBlock )
    flags |= O_NONBLOCK;
  else
    flags &= ~O_NONBLOCK;

  SetFlags( flags );
}


bool File::SyncWrite() const
{
  int flags;

  if ( GetFlags( flags ) != 0 )
    return false;

  return flags & O_SYNC;
}


void File::SyncWrite( bool fSync ) const
{
  int flags;

  if ( GetFlags( flags ) != 0 )
    return;

  if ( fSync )
    flags |= O_SYNC;
  else
    flags &= ~O_SYNC;

  SetFlags( flags );
}


bool File::Async() const
{
  int flags;

  if ( GetFlags( flags ) != 0 )
    return false;

  return flags & O_ASYNC;
}


void File::Async( bool fAsync ) const
{
  int flags;

  if ( GetFlags( flags ) != 0 )
    return;

  if ( fAsync )
    flags |= O_ASYNC;
  else
    flags &= ~O_ASYNC;

  SetFlags( flags );
}


int File::GetOwnerProcessOrGroup( pid_t& pid ) const
{
  int iRetVal;

  if ( (iRetVal = fcntl( m_nDescriptor, F_GETOWN )) == -1 )
    {
      pid = 0;
      return errno;
    }

  pid = iRetVal;
  return 0;
}


int File::SetOwnerProcess( pid_t pid ) const
{
  if ( fcntl( m_nDescriptor, F_SETOWN, long(pid) ) != 0 )
    return errno;

  return 0;
}


int File::Ioctl( int iRequest ) const
{
  if ( ioctl( m_nDescriptor, iRequest ) != 0 )
    return errno;

  return 0;
}


int File::Ioctl( int iRequest, void *pvArg ) const
{
  if ( ioctl( m_nDescriptor, iRequest, pvArg ) != 0 )
    return errno;

  return 0;
}


int File::Stat( struct stat& StatStruct ) const
{
  if ( fstat( m_nDescriptor, &StatStruct ) != 0 )
    return errno;

  return 0;
}


int File::ChangeMode( mode_t mode ) const
{
  if ( fchmod( m_nDescriptor, mode ) != 0 )
    return errno;

  return 0;
}


int File::ChangeOwnerAndGroup( uid_t uidOwner, gid_t gidGroup ) const
{
  if ( fchown( m_nDescriptor, uidOwner, gidGroup ) != 0 )
    return errno;

  return 0;
}


int File::Truncate( off_t Length ) const
{
  if ( ftruncate( m_nDescriptor, Length ) != 0 )
    return errno;

  return 0;
}


int File::Sync() const
{
  if ( fsync( m_nDescriptor ) != 0 )
    return errno;

  return 0;
}


int File::DataSync() const
{
  if ( fsync( m_nDescriptor ) != 0 )
    return errno;

  return 0;
}


int File::GetRecordLock( const struct flock& FLockStructInput, struct flock& FLockStructOutput ) const
{
  FLockStructOutput = FLockStructInput;

  if ( fcntl( m_nDescriptor, F_GETLK, &FLockStructOutput ) != 0 )
    return errno;

  return 0;
}


int File::SetRecordLock( const struct flock& FLockStruct, bool fWait ) const
{
  if ( fcntl( m_nDescriptor, fWait ? F_SETLKW : F_SETLK, &FLockStruct ) != 0 )
    return errno;

  return 0;
}


bool File::IsRangeReadLockable( off_t Offset, int iWhence, size_t Length, pid_t& pid ) const
{
  struct flock In, Out;

  In.l_type = F_RDLCK;
  In.l_start = Offset;
  In.l_whence = iWhence;
  In.l_len = Length;

  if ( GetRecordLock( In, Out ) != 0 )
    return false;

  if ( Out.l_type == F_UNLCK )
    {
      pid = 0;
      return true;
    }
  else
    {
      pid = Out.l_pid;
      return false;
    }
}


bool File::IsRangeWriteLockable( off_t Offset, int iWhence, size_t Length, pid_t& pid ) const
{
  struct flock In, Out;

  In.l_type = F_WRLCK;
  In.l_start = Offset;
  In.l_whence = iWhence;
  In.l_len = Length;

  if ( GetRecordLock( In, Out ) != 0 )
    return false;

  if ( Out.l_type == F_UNLCK )
    {
      pid = 0;
      return true;
    }
  else
    {
      pid = Out.l_pid;
      return false;
    }
}


int File::ReadLockRange( off_t Offset, int iWhence, size_t Length ) const
{
  struct flock l;

  l.l_type = F_RDLCK;
  l.l_start = Offset;
  l.l_whence = iWhence;
  l.l_len = Length;

  return SetRecordLock( l );
}


int File::WriteLockRange( off_t Offset, int iWhence, size_t Length ) const
{
  struct flock l;

  l.l_type = F_WRLCK;
  l.l_start = Offset;
  l.l_whence = iWhence;
  l.l_len = Length;

  return SetRecordLock( l );
}


int File::ReadLockRangeWait( off_t Offset, int iWhence, size_t Length ) const
{
  struct flock l;

  l.l_type = F_RDLCK;
  l.l_start = Offset;
  l.l_whence = iWhence;
  l.l_len = Length;

  return SetRecordLock( l, true );
}


int File::WriteLockRangeWait( off_t Offset, int iWhence, size_t Length ) const
{
  struct flock l;

  l.l_type = F_WRLCK;
  l.l_start = Offset;
  l.l_whence = iWhence;
  l.l_len = Length;

  return SetRecordLock( l, true );
}


int File::UnlockRange( off_t Offset, int iWhence, size_t Length ) const
{
  struct flock l;

  l.l_type = F_UNLCK;
  l.l_start = Offset;
  l.l_whence = iWhence;
  l.l_len = Length;

  return SetRecordLock( l );
}
