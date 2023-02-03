package hello.core.member;

//구현체가 하나일 경우 인터페이스명+Impl 쓰는 것이 관례
public class MemberServiceImpl implements MemberService {

    //DIP 위반
    //MemberServiceImpl은 MemberRepository(인터페이스) 뿐만 아니라 MemoryMemberRepository(구현체)에도 의존
    private final MemberRepository memberRepository = new MemoryMemberRepository();

    @Override
    public void join(Member member) {
        memberRepository.save(member);
    }

    @Override
    public Member findMember(Long memberId) {
        return memberRepository.findById(memberId);
    }
}
